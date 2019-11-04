class node:    
    
    # Node basic data: Author, date, published etc
    authorName = ""
    #technical nodeData
    
    websiteReferences = []
    articleReferences = []
    articlesReferenced = []
    predecessors = []
    successors = []
    #Node Methods
    def __init__(self):
        self.authorName = "Root"
        self.websiteReferences = []
        self.articleReferences = []
        self.articlesReferenced = []
        self.predessors = []
        self.successors = []
    def __init__(self,name,websiteRefs,articleRefs,articleRefd,predecessors,successors):
        self.authorName = name
        self.websiteReferences = websiteRefs
        self.articleReferences = articleRefs
        self.articlesReferenced = articleRefd


class Multiwaytree:
    ## The tree has a dummy node at the top to connect all the subtrees
    ## The n=1 layer has the website dummy nodes representing the respective subtrees
    ## Every article node will be placed in one of these subtrees based on a priority list given to websites based on alphabetical order.
    ## the alphabetical ranking is temporary. This will be changed after some preprocessing on data.
    ## in the preprocessing step, we rank the websites based on maximum number of articles that reference it. 
    ## If an article refers to multiple websites, then the additional websites will be placed in an additional list 
    ## This is done to eliminate unnecessary relationships in the tree. 
    
    #Tree Level 0 and 1

    root = node("Root",[],[],[],[],[])
    facebookMaster = node("facebook",[],[],[],[],[])
    twitterMaster = node("twitter",[],[],[],[],[])
    redditMaster = node("reddit",[],[],[],[],[])
    websiteNodeList = [facebookMaster,twitterMaster,redditMaster] 
    #Tree Methods
    def __init__(self,nodeArray):
        self.root.successors = [facebookMaster,twitterMaster,redditMaster]
        self.facebookMaster.predecessors = [root]
        self.twitterMaster.predecessors = [root]
        self.redditMaster.predecessors = [root]

        # We find the first website in the sorted list of websites for each node
        # Each website has a subtree of its own.
        # First we look to see if any of the node's parents belong to the same website subtree.
        # if any of the node's parents are in the same subtree then we add the node as successor to this parent node.
        # else we add the node as successor to the subtree's dummy node.
        for node in nodeArray:
            node.websiteReferences.sort()
            websiteName = node.websiteReferences[0]
            
            for websiteNode in websiteNodeList:
                if (websiteName == websiteNode.authorName):
                    if(len(websiteNode.successors)==0):
                       addBranch(websiteNode,node)
                    
                    else:
                        for predecessor in node.predessors:
                            if (websiteNode == getTopRankWebsite(predecessor)):
                                addBranch(predecessor,node)

                    

    def addBranch(self,predessorNode,successorNode):
        predessorNode.successors.append(successorNode)
        successorNode.predecessors.append(predessorNode)

    def getTopRankWebsite(self,inputNode):
        inputNode.websiteReferences.sort()
        return inputNode.websiteReferences[0]

